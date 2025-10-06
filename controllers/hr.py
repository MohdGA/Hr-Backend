from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.hr import hrModel
from models.user import UserModel
from serializers.hr import hrSchema, hrCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get('/Hrs', response_model=List[hrSchema])
def get_hr(db: Session = Depends(get_db)):
    hr = db.query(hrModel).all()
    return hr

@router.get('/Hrs/{hr_id}', response_model=hrSchema)
def get_single_hr(hr_id: int, db: Session = Depends(get_db)):
    
    hr = db.query(hrModel).filter(hrModel.id == hr_id).first()

    if not hr:
        raise HTTPException(status_code=404, detail="hr not found")
    return hr

@router.post('/Hrs', response_model=hrSchema)
def create_hr(hr: hrCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_hr = hrModel(**hr.dict(), user_id = current_user.id)
    db.add(new_hr)
    db.commit()
    db.refresh(new_hr)
    return new_hr

@router.put('/Hrs/{hr_id}', response_model=hrSchema)
def update_hr(hr_id: int, hr: hrCreateSchema, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_hr = db.query(hrModel).filter(hrModel.id == hr_id).first()

    if not db_hr:
        raise HTTPException(status_code=404, detail="hr not found")
    
    if db_hr.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    hr_data = hr.dict(exclude_unset=True)  # only updated the fields provided

    for key, value in hr_data.items():
        setattr(db_hr, key, value)

    db.commit()
    db.refresh(db_hr)
    return db_hr

@router.delete('/Hrs/{hr_id}')
def remove_hr(hr_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_hr = db.query(hrModel).filter(hrModel.id == hr_id).first()

    if not db_hr:
        raise HTTPException(status_code=404, detail="hr not found")
    
    if not db_hr.user_id == current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    db.delete(db_hr)
    db.commit()
    return {"message": f"Hr with ID {hr_id} has been removed"}