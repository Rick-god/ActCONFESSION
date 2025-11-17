from bot.models.user import User, USERROLE
from bot.models.comment import Comment, CommentReaction
from bot.models.confession import Confessions
from sqlalchemy.orm import Session
from config import ANONYMITY_SALT as secret_salt
import hashlib
import os

def generate_anonymous_id(telegram_id: int) -> str:
    unique_string = f"{telegram_id}{secret_salt}"
    return hashlib.sha256(unique_string.encode()).hexdigest()[:16]

def create_user(db: Session, telegram_id: int) -> User:
    telegram_hash = generate_anonymous_id(telegram_id)
    
    existing_user = db.query(User).filter(User.telegram_id_hash == telegram_hash).first()
    if existing_user:
        return existing_user
    
    profile_id = generate_unique_profile_id(db)
    
    new_user = User(
        telegram_id_hash=telegram_hash,
        unique_id=profile_id,
        name="Anonymous",
        bio="No bio",
        points=0,
        role=UserRole.USER
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_telegram_id(db: Session, telegram_id: int):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    return user

def get_user_by_profile_id(db: Session, profile_id: str):
    user = db.query(User).filter(User.unique_id == profile_id).first()
    return user

def update_user_points(db: Session, unique_id: str, pts_change: int):
    user = db.query(User).filter(User.unique_id == unique_id).first()
    if user:
        user.points += pts_change
        db.commit()
        db.refresh(user)
    return user

def create_confession(db: Session, confession_text: str, confessor_id: str) -> Confessions:
    new_confession = Confessions(
        confession_message=confession_text,
        confessor_id = confessor_id,
        status = "pending"
    )
    db.add(new_confession)
    db.commit()
    db.refresh(new_confession)
    return new_confession

def get_pending_confessions(db: Session):
    pending_confessions = db.query(Confessions).filter(Confessions.status=="pending").all()
    return pending_confessions

def approve_confession(db: Session, confession_id: int, validator_id: int):
    confession = db.query(Confessions).filter(Confessions.id==confession_id).first()
    if validator_id:
        confession.validator_id = validator_id

    if confession.status == "pending":
        confession.status = "approved"
        db.commit()
        db.refresh(confession)

def add_comment(db: Session, commenter_id: str, confession_id: int, comment_content: str, media_file_id: str = None, main_comment_id: int = None) -> Comment:
    new_comment = Comment(
        comment_content=comment_content,
        confession_id=confession_id,
        commenter_id=commenter_id,
        media_file_id=media_file_id,
        main_comment_id=main_comment_id,
        likes_count=0,
        dislikes_count=0
    )
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def add_comment_reaction(db: Session, comment_id: int, user_id: int, reaction_type: str) -> CommentReaction:
    existing_reaction = db.query(CommentReaction).filter(CommentReaction.comment_id == comment_id,CommentReaction.user_id == user_id).first()
    
    if existing_reaction:
        existing_reaction.reaction_type = reaction_type
        db.commit()
        db.refresh(existing_reaction)
        return existing_reaction
    else:
        new_reaction = CommentReaction(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type
        )
        db.add(new_reaction)
        db.commit()
        db.refresh(new_reaction)
        return new_reaction

