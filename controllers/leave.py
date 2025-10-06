from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.leave import leaveModel
from models.hr import hrModel
from serializers.leave import leaveCreateSchema, leaveSchema
from typing import List
from database import get_db

router = APIRouter()

@router.get('/Hrs/{hr_id}/leaves', response_model=List[leaveSchema])
def get_leaves(db:Session = Depends(get_db)):
    leave = db.query(leaveModel).all()
    return leave


@router.get('/leaves/{leave_id}', response_model=leaveSchema)
def get_a_leave(leave_id: int, db: Session = Depends(get_db)):

    leave = db.query(leaveModel).filter(leaveModel.id == leave_id).first()

    if not leave:
        raise HTTPException(status_code=404, detail='leave not found')
    
    return leave


@router.post('/Hrs/{hr_id}/leaves', response_model=leaveSchema)
def create_leaves(hr_id: int, leave: leaveCreateSchema ,db: Session = Depends(get_db)):
    hr = db.query(hrModel).filter(hrModel.id == hr_id).first()

    if not hr:
        raise HTTPException(status_code=404, detail="hr not found")

    new_leave = leaveModel(**leave.dict(), hr_id = hr_id)

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave

@router.delete('/Hrs/leaves/{leave_id}')
def remove_leave(leave_id: int, db: Session = Depends(get_db)):
    db_leave = db.query(leaveModel).filter(leaveModel.id == leave_id).first()

    if not db_leave:
        raise HTTPException(status_code=404, detail='leave not found')
    
    db.delete(db_leave)
    db.commit()
    return {'message': f"leave with ID {leave_id} has been deleted"}

