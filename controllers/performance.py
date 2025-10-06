from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.performance import performanceModel
from models.hr import hrModel
from serializers.performance import performanceSchema, performanceCreateSchema
from typing import List
from database import get_db

router = APIRouter()

@router.get('/Hrs/{hr_id}/performance', response_model=List[performanceSchema])
def get_performance(db: Session = Depends(get_db)):
    performance = db.query(performanceModel).all()
    return performance

@router.post('/Hrs/{hr_id}/performance', response_model=performanceSchema)
def create_performance(hr_id: int, performance: performanceCreateSchema, db: Session = Depends(get_db)):
    hr = db.query(hrModel).filter(hrModel.id == hr_id).first()

    if not hr:
        raise HTTPException(status_code=404, detail='hr not found')
    
    new_performance = performanceModel(**performance.dict(), hr_id = hr_id)

    db.add(new_performance)
    db.commit()
    db.refresh(new_performance)

    return new_performance

@router.delete('/Hrs/performance/{performance_id}')
def remove_performance(performance_id: int, db: Session = Depends(get_db)):
    db_performance = db.query(performanceModel).filter(performanceModel.id == performance_id).first()

    if not db_performance:
        raise HTTPException(status_code=404, detail="performance not found")
    
    db.delete(db_performance)
    db.commit()
    return {'message': f"performance with ID {performance_id} has been deleted"}
