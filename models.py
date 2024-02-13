from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db=SQLAlchemy()

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String, unique=True,nullable=False)
    password=db.Column (db.String, nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    fitness_goals=db.Column(db.String)

    #rel
    user_challenge_progress=db.relationship('UserChallengeProgress',back_populates='user',lazy=True)
    challenge=db.relationship('Challenge',back_populates='user')

    #validations
    @validates('username')
    def validate_username(self,key,users):
        if not users:
            raise ValueError("All users must have a username")
        return users

    @validates('email')
    def validate_email(self,key,users):
        if '@' not in users:
            raise ValueError("failed simple email validation")
        return users


    def __repr__(self):
        return f"{self.username},{self.email}{self.fitness_goals}"
    

class Challenge(db.Model):
    __tablename__='challenges'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    description=db.Column(db.Text, nullable=False)
    start_date=db.Column(db.Integer,nullable=False)
    end_date=db.Column(db.Integer,nullable=False)
    creator_id= db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

    #rel
    user_challenge_progress=db.relationship('UserChallengeProgress',back_populates='challenge',lazy=True)
    user=db.relationship('User',back_populates='challenge')

    #validations
    @validates('title')
    def validate_title(self,key,challenges):
        if not challenges:
            raise ValueError("Challenge must have a title")
        return challenges

    def __repr__(self):
        return f"{self.title},{self.description}{self.start_date},{self.end_date},{self.creator_id}"
    
class UserChallengeProgress(db.Model):
    __tablename__='user_challenge_progresses'

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    challenge_id=db.Column(db.Integer,db.ForeignKey('challenges.id'),nullable=False)
    progress=db.Column(db.Integer,nullable=False) 
    completed=db.Column(db.String,nullable=False)

    #rel
    user=db.relationship('User',back_populates='user_challenge_progress',lazy=True)
    challenge=db.relationship('Challenge',back_populates='user_challenge_progress',lazy=True)
    
    #validations
    @validates('completed')
    def validates_completed(self,key,user_challenge_progresses):
        if user_challenge_progresses not in ['Yes','Not yet started','Not yet finished']:
            raise ValueError("Choose among: 'Yes','Not yet started','Not yet finished'")
        return user_challenge_progresses

    def __repr__(self):
        return f"{self.user_id},{self.challenge_id}{self.progress},{self.completed}"
