from faker import Faker

faker = Faker()

for k in range(20):
    print(
        {
            'uuid': faker.uuid4(),
            'name': faker.name(),
            'address': faker.address(),
        }
    )
