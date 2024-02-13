from flask import Flask,make_response,request,jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db,User, Challenge,UserChallengeProgress

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

CORS(app)
migrate=Migrate(app,db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/users',methods=['GET'])
def get_users():
    users=User.queryy.all()
    users_data=[
        {"id":user.id,"username":user.username,"fitness_goals":user.fitness_goals}
        for user in users
    ]
    response=make_response(
        jsonify (users_data),
        200
    )
    return response

@app.route('/users/<int:id>',methods=['GET'])
def get_users_by_id(id):
    user=User.query.filter(User.id==id).first()

    if request.method=='GET':
        user_dict=user.to_dict()

        response=make_response(
            jsonify(user_dict),
            200
        )
        return response
    if user is None:
        response=make_response({"error":"User not found"},
        404
        )
        return response

@app.route('/challenges', methods=['GET'] )
def get_challenges():
    
        challenges=Challenge.query.all()
        challenges_data=[
             {"creator_id":challenge.creator_id, "title":challenge.title, "description":challenge.description}
             for challenge in challenges
        ]

        response=make_response(
             jsonify(challenges_data),
             200
        )
        return response

@app.route ('/challenges/<int:id>',methods=['GET'])
def get_challenges_by_id(id):
    
    if request.method == 'GET':
        challenge = Challenge.query.filter(Challenge.id ==id).first() 

    if not challenge:
        response=make_response( jsonify({"Error":"Task not Found"}),404
        )
        return response
        
    response=make_response(
        jsonify(challenge.to_dict()),
        200
    )
    return response

@app.route('/my-challenges/<int:id>',methods=['GET','DELETE','POST','PATCH'])
def get_progress_by_id(id):
    if request.method == 'GET':
        progress=UserChallengeProgress.query.filter(UserChallengeProgress.id == id).first()

    if not progress:
        response=make_response(jsonify({"Error":"Task not Found!"}),404
        )
        return response
    
    response= make_response(jsonify(progress.to_dict()),
    200
    )

    if request.method == 'DELETE':
        db.session.delete(progress)
        db.session.commit()

        response=make_response(
            jsonify({"Progress Deleted"}),
            200
        )

    if request.method == 'POST':
        new_progress= UserChallengeProgress(
            challenge_id=request.form.get('challenge_id'),
            progress=request.form.get('user_id'),
            completed=request.form.get('completed'),
        )
        db.session.add(new_progress)
        db.session.commit()

        response=make_response(
            jsonify(new_progress.to_dict()),
            200
        )
        response.headers['Content-Type']
        return response

    if request.method == 'PATCH':
        progress=UserChallengeProgress.query.filter_by(id==id).first()

        for attr in request.form:
            setattr(progress,attr,request.form.get(attr))
        db.session.add(progress)
        db.session.commit()

        progress_dict=progress.to_dict()

        response=make_response(
            jsonify(progress_dict),
            200
        )
        return response
    

if __name__ == '__main__':
    app.run(port=5555)