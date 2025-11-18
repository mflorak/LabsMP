import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os


def get_rates_range(currency_code='usd', days=7):

    end_date = datetime.now() - timedelta(days=1)
    start_date = end_date - timedelta(days=days - 1)

    start_str = start_date.strftime("%Y%m%d")
    end_str = end_date.strftime("%Y%m%d")

    url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    params = {
        'start': start_str,
        'end': end_str,
        'valcode': currency_code,
        'sort': 'exchangedate',
        'order': 'asc',
        'json': 'json'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Помилка при отриманні даних: {e}")
        return []


currency = 'usd'
data = get_rates_range(currency)

# 1. ВИВІД КУРСУ В ТЕРМІНАЛ (завдання 2)
print(f"\n📈 Отримання курсу {currency.upper()} за останній тиждень...")
if data:
    for item in data:
        rate = item['rate']
        date = item['exchangedate']
        print(f"{date}: {rate} грн")
else:
    print("Не вдалося отримати дані про курси валют.")

# 2. ПІДГОТОВКА ДАНИХ ТА ПОБУДОВА ГРАФІКА (завдання 3)
if data:
    dates = [datetime.strptime(item['exchangedate'], '%d.%m.%Y').strftime('%d.%m') for item in data]
    rates = [item['rate'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker='o', linestyle='-', color='g', label=f'Курс {currency.upper()}')
    plt.title(f'Динаміка курсу {currency.upper()} НБУ за тиждень')
    plt.xlabel('Дата')
    plt.ylabel('Курс (UAH)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = 'screens/currency_dynamic.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)

    print(f"\n✅ Графік '{output_path}' успішно сгенеровано та збережено.")