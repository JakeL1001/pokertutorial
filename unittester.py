import unittest

from werkzeug.security import generate_password_hash
from pokerapp import pokerpack, db
from pokerapp.models import User, Results

class UserModelCase(unittest.TestCase):
    
    unittest.TestLoader.sortTestMethodsUsing = None
    
    def test_1_setup(self):
        self.pokerpack = pokerpack.test_client()
        db.create_all()
        User1 = User(id="930", username="testuser1", email="testuser1@example.com")
        User2 = User(id="931", username="testuser2", email="testuser2@example.com")
        User3 = User(id="932", username="testuser3", email="testuser3@example.com")
        Result1 = Results(user_id="930", quiz1="50", quiz2="60", quiz3="75", finalquiz="50")
        Result2 = Results(user_id="931", quiz1="55", quiz2="75", quiz3="90", finalquiz="75")
        Result3 = Results(user_id="932", quiz1="75", quiz2="95", quiz3="80", finalquiz="70")
        db.session.add(User1)
        db.session.add(User2)
        db.session.add(User3)
        db.session.add(Result1)
        db.session.add(Result2)
        db.session.add(Result3)
        db.session.commit()

    def test_2_user_password_hash(self):
        u1 = User.query.get("930")
        u2 = User.query.get("931")
        u1.set_password("testpassword")
        u2.set_password("notpassword")
        self.assertFalse(u1.check_password("notpassword"))
        self.assertFalse(u1.check_password("alsonotpassword"))
        self.assertTrue(u1.check_password("testpassword"))
        self.assertTrue(u2.check_password("notpassword"))
        
    def test_3_undo_setup(self):
        self.pokerpack = pokerpack.test_client()
        User.query.filter_by(id="930").delete()
        User.query.filter_by(id="931").delete()
        User.query.filter_by(id="932").delete()
        Results.query.filter_by(user_id="930").delete()
        Results.query.filter_by(user_id="931").delete()
        Results.query.filter_by(user_id="932").delete()
        db.session.commit()
        
if __name__ == '__main__':
    unittest.main()