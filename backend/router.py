"""
router.py: Routes incoming requests to the appropriate endpoint handlers
"""
from fastapi import APIRouter
import endpoint

router = APIRouter()

router.include_router(endpoint.router, prefix="/events", tags=["events"]) # Prefixes each handler with events. See endpoint