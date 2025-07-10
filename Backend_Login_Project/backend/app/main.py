from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ Add this
from app.api import user_api, verse_api
from app.core.database_core import create_db

app = FastAPI(title="Bhagavad Gita Reader API")

# ✅ ALLOW frontend origin (adjust as needed)
origins = [
    "https://sturdy-spoon-r4654jp7q6gw359vq-3000.app.github.dev"  # ✅ GitHub Codespace frontend
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # ✅ Frontend URLs allowed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Include routers
app.include_router(user_api.router, prefix="/user", tags=["User"])
app.include_router(verse_api.router, prefix="/verse", tags=["Verse"])

# Startup
@app.on_event("startup")
def on_startup():
    create_db()
