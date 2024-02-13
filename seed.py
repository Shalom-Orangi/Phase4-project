from random import choice, randint
from app import app
from faker import Faker

from models import db, User,Challenge,UserChallengeProgress

fake=Faker()

with app.app_context():
    User.query.delete()
    Challenge.query.delete()
    UserChallengeProgress.query.delete()

#Seed Users
    users=[]
    for _ in range(15):
        user=User(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
            fitness_goals=fake.text(),
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

#seed Challenges
    challenges_data=[
        {
            "title": "30-Day Cardio Blast",
            "description": "Challenge yourself to 30 days of intense cardio exercises to improve your cardiovascular health and endurance."
        },
        {
            "title": "Core Strength Challenge",
            "description": "Focus on building a strong core with a series of exercises targeting your abdominal muscles, obliques, and lower back."
        },
        {
            "title": "Yoga and Mindfulness Journey",
            "description": "Embark on a 4-week yoga and mindfulness challenge to enhance flexibility, balance, and mental well-being."
        },
        {
            "title": "Strength Training Bootcamp",
            "description": "Join the strength training bootcamp and engage in a variety of exercises to build muscle mass and overall strength."
        },
        {
            "title": "Couch to 5K Running Challenge",
            "description": "Begin your running journey with a structured 8-week plan, progressing from walking to running a 5K distance."
        },
        {
            "title": "Full-Body HIIT Challenge",
            "description": "Experience high-intensity interval training (HIIT) with a mix of cardio and strength exercises for a full-body workout."
        },
        {
            "title": "Flexibility and Stretching Quest",
            "description": "Dedicate 3 weeks to improve flexibility through daily stretching routines, enhancing your range of motion."
        },
        {
            "title": "Outdoor Adventure Fitness",
            "description": "Combine fitness with outdoor adventure by incorporating activities like hiking, biking, and kayaking into your routine."
        },
        {
            "title": "Plank-a-Day Challenge",
            "description": "Challenge yourself to hold a plank position every day, gradually increasing the duration for improved core stability."
        },
        {
            "title": "Meditation and Relaxation Challenge",
            "description": "Explore the benefits of meditation and relaxation techniques in this 2-week challenge for stress reduction and mental clarity."
        },
    ]
       
    challenges=[]
    for challenge_data in challenges_data:
        challenge=Challenge(
            **challenge_data,
            start_date=randint(0,31),
            end_date=randint(0,31),
            creator_id=randint (0,15),
            )
        challenges.append(challenge)

    db.session.add_all(challenges)
    db.session.commit()

#seed userchallengeprogress
    users=User.query.all()
    challenges=Challenge.query.all()    

    for user in users:
        for challenge in challenges:
            progress= randint(0,100)
            completed= choice (['Yes','Not yet started','Not yet finished'])

            user_challenge_progress=UserChallengeProgress (
                    
                user_id=user.id,
                challenge_id=challenge.id,
                progress=progress,
                completed=completed,
            )
            db.session.add(user_challenge_progress)
    
        db.session.commit()


    print("Database seeded successfully.")