'''
python manage.py shell
execute the below command inside the shell
exec(open('./persons_app/dbscripts/populate_persons.py').read())
'''

from faker import Faker
from persons_app.models import Person
MAX_LIMIT = 1000
AGES = [i for i in range(1, 99)]
fake = Faker()

class PopulatePerson:
    
    def __init__(self) -> None:
        pass
    
    def fetch_random_age(self):
        return fake.random_choices(elements=AGES, length=1)
    
    def run(self):
        for i in range(1, MAX_LIMIT):
            name = fake.name()
            age = self.fetch_random_age()[0]
            print("i", i)
            print("name", name)
            print("age", age)
            person_obj = Person.objects.create(
                name=name,
                age=age
            )
            print("person", person_obj)
    
populate_person = PopulatePerson()
populate_person.run()