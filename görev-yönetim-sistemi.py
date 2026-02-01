from database import create_tables, add_user, add_task, get_tasks


def main():
    create_tables()

    while True:
        print("\n--- Menü Sistemi ---")
        print("1 - Kullanıcı oluştur")
        print("2 - Görev ekle")
        print("3 - Görevleri listele")
        print("4 - Çıkış")

        secim = input("Seçiminiz: ")

        try:
            if secim == "1":
                username = input("Kullanıcı adı: ")
                add_user(username)

            elif secim == "2":
                user_id = int(input("Kullanıcı ID: "))
                task = input("Görev adı: ")
                add_task(user_id, task)

            elif secim == "3":
                user_id = int(input("Kullanıcı ID: "))
                tasks = get_tasks(user_id)

                print(f"\n--- {user_id} ID'li Kullanıcının Görevleri ---")
                if not tasks:
                    print("Görev bulunamadı.")
                else:
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task[0]}")

            elif secim == "4":
                print("Çıkış yapılıyor...")
                break

            else:
                print("Geçersiz seçim.")

        except ValueError:
            print("Lütfen sayısal değer girin.")
        except Exception as e:
            print("Bir hata oluştu:", e)

if __name__ == "__main__":
    main()