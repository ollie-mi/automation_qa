import requests


class PetStore:

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'

    def get_available_pets(self) -> requests:
        """Get all available pets"""
        url = self.base_url + '/pet/findByStatus'
        status = 'available'
        query = {'status': status}
        r = requests.get(url, params=query)
        return r

    def post_new_pet(self, name: str, category_name: str) -> requests:
        """Add new pet to the store"""
        if not name or not category_name:
            raise ValueError("name or category_name are empty!")
        elif not isinstance(name, str) or not isinstance(category_name, str):
            raise ValueError("name and category_name should be strings!")

        url = self.base_url + '/pet'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = {
            "id": 0,
            "category": {"id": 0, "name": category_name},
            "name": name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
        r = requests.post(url, headers=headers, json=data)
        return r

    def get_pet_by_id(self, pet_id: int) -> requests:
        """Get pet by id. If not found returns 404"""
        if not isinstance(pet_id, int):
            raise ValueError("pet_id should be integer")
        url = self.base_url + '/pet/' + str(pet_id)
        r = requests.get(url)
        return r

    def delete_pet_by_id(self, pet_id: int) -> requests:
        """Delete pet by id"""
        if not isinstance(pet_id, int):
            raise ValueError("pet_id should be integer")
        url = self.base_url + '/pet/' + str(pet_id)
        r = requests.delete(url)
        return r


if __name__ == '__main__':
    pet_store = PetStore()

    avail_pets = pet_store.get_available_pets()
    print(avail_pets.status_code)
    print(avail_pets.text)

    add_pet = pet_store.post_new_pet('Marsik', 'cat')
    print(add_pet.status_code)
    print(add_pet.text)

    get_pet = pet_store.get_pet_by_id(9223372036854765223)
    print(get_pet.status_code)
    print(get_pet.text)

    delete_pet = pet_store.delete_pet_by_id(9223372036854770902)
    print(delete_pet.status_code)
    print(delete_pet.text)
