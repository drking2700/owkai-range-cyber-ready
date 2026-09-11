from __future__ import annotations
import os
from urllib.parse import urlencode
import httpx
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from .db import ensure_learner

router = APIRouter(prefix="/auth")

GITHUB_AUTHORIZE = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN = "https://github.com/login/oauth/access_token"
GITHUB_USER = "https://api.github.com/user"


def current_learner(request: Request) -> str:
    return (
        request.session.get("learner_id")
        or request.headers.get("X-Range-Learner")
        or request.cookies.get("range_learner")
        or "demo"
    )


@router.get("/github")
def github_login(request: Request):
    client_id = os.getenv("GITHUB_CLIENT_ID", "")
    if not client_id:
        raise HTTPException(503, "GitHub OAuth is not configured; local learner mode remains available.")
    state = os.urandom(16).hex()
    request.session["oauth_state"] = state
    params = {
        "client_id": client_id,
        "redirect_uri": os.getenv("GITHUB_CALLBACK_URL", "http://127.0.0.1:8000/auth/github/callback"),
        "scope": "read:user user:email",
        "state": state,
    }
    return RedirectResponse(GITHUB_AUTHORIZE + "?" + urlencode(params))


@router.get("/github/callback")
def github_callback(request: Request, code: str, state: str):
    if not request.session.get("oauth_state") or state != request.session.pop("oauth_state"):
        raise HTTPException(400, "Invalid OAuth state")
    client_id = os.getenv("GITHUB_CLIENT_ID", "")
    client_secret = os.getenv("GITHUB_CLIENT_SECRET", "")
    if not (client_id and client_secret):
        raise HTTPException(503, "GitHub OAuth is not configured")
    with httpx.Client(timeout=20) as client:
        token = client.post(
            GITHUB_TOKEN,
            headers={"Accept": "application/json"},
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "redirect_uri": os.getenv("GITHUB_CALLBACK_URL", "http://127.0.0.1:8000/auth/github/callback"),
            },
        )
        token.raise_for_status()
        access_token = token.json().get("access_token")
        if not access_token:
            raise HTTPException(400, "GitHub did not return an access token")
        user = client.get(
            GITHUB_USER,
            headers={"Authorization": f"Bearer {access_token}", "Accept": "application/vnd.github+json"},
        )
        user.raise_for_status()
        profile = user.json()
    learner_id = f"github:{profile['id']}"
    display = profile.get("name") or profile.get("login") or learner_id
    ensure_learner(learner_id, display)
    request.session["learner_id"] = learner_id
    request.session["display_name"] = display
    # Deliberately do not persist OAuth access tokens in V1.
    return RedirectResponse("/")


@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/")
