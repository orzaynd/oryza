import requests

class APIClient:
    def __init__(self, url):  # Perbaikan di sini
        self.url = url
        self.data = []
        self.current_page = 0
        self.page_size = 10

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Failed to fetch data:", response.status_code)  # Pindah ke else

    def display_data(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        page_data = self.data[start_index:end_index]

        if not page_data:
            print("No more data to display.")
            return
        
        for item in page_data:  # Perbaikan indentasi di sini
            print(item)

    def next_page(self):
        if (self.current_page + 1) * self.page_size < len(self.data):
            self.current_page += 1
        else:
            print("You are already on the last page.")

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("You are already on the first page.")

    def reverse_data(self):
        self.data.reverse()

if __name__ == "__main__":  # Perbaikan di sini
    api_url = "https://jsonplaceholder.typicode.com/posts"  
    client = APIClient(api_url)
    client.fetch_data()
    
    while True:
        print("\nData Halaman:")
        client.display_data()
        command = input("\nMasukkan perintah (next, prev, reverse, exit): ").strip().lower()

        if command == "next":
            client.next_page()
        elif command == "prev":
            client.previous_page()
        elif command == "reverse":
            client.reverse_data()
        elif command == "exit":
            break
        else:
            print("Perintah tidak dikenali.")