from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Item, Category, Users

engine = create_engine('postgresql://catalog:catalog@localhost/itemcatalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


User1 = Users(name="Test Account", email="testaccount@gmail.com")
session.add(User1)
session.commit()


category1 = Category(user_id=1, name="RPG")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Pokemon", description="Pokemon is a series of \
    video games developed by Game Freak and published by Nintendo and The \
    Pokemon Company as part of the Pokemon media franchise.",
             category=category1)


session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Skyrim", description="The Elder Scrolls V: \
    Skyrim is an action role-playing video game developed by Bethesda Game \
        Studios and published by Bethesda Softworks.",
	     category=category1)


session.add(item2)
session.commit()


category2 = Category(user_id=1, name="FPS")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Counter Strike", description="Counter-Strike \
    (CS) is a series of multiplayer first-person shooter video games, in \
        which teams of terrorists battle to perpetrate an act of terror ",
	     category=category2)


session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Battlefield", description="Battlefield is a \
    series of first-person shooter video games that started out on Microsoft \
        Windows and OS X with Battlefield 1942, which was released in 2002.",
             category=category2)


session.add(item2)
session.commit()

category3 = Category(user_id=1, name="RTS")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="StarCraft", description="StarCraft is a \
    military science fiction media franchise, created by Chris Metzen \
        and James Phinney and owned by Blizzard Entertainment.",
             category=category3)


session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Age of Empires", description="Age of Empires\
     is a series of historical real-time strategy video games, originally \
         developed by Ensemble Studios and published by Xbox Game Studios.",
             category=category3)


session.add(item2)
session.commit()
