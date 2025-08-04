# member_routes.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.member import Member
from member_module.member_db_operations import MemberOperations

router = APIRouter(prefix="/members", tags=["members"])

def get_member_operations():
    return MemberOperations()

@router.get("/", response_model=List[Member])
async def get_all_members(member_ops: MemberOperations = Depends(get_member_operations)):
    """Get all members"""
    try:
        members = await member_ops.get_all_members()
        return members
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{member_id}", response_model=Member)
async def get_member_by_id(member_id: str, member_ops: MemberOperations = Depends(get_member_operations)):
    """Get member by ID"""
    try:
        member = await member_ops.get_member_by_id(member_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        return member
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/by-plan/{plan_type}", response_model=List[Member])
async def search_members_by_plan(plan_type: str, member_ops: MemberOperations = Depends(get_member_operations)):
    """Search members by plan type"""
    try:
        # Get all and filter (you can add a specific method in MemberOperations for better performance)
        all_members = await member_ops.get_all_members()
        filtered_members = [member for member in all_members if member.planType.lower() == plan_type.lower()]
        return filtered_members
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))