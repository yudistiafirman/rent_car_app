from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns 


def display_car_list(cars):
    console = Console()
    car_panels = []

    for index, car in enumerate(cars, start=1):
        car_table = Table.grid(padding=(1, 2))
        car_table.add_column(justify="left", width=20)
        car_table.add_row(Panel("Foto", style="bold white on black", expand=True, width=25, height=10))
        car_table.add_row(f"[bold]{car.name} {car.jenis_transmisi.value}[/bold]")
        car_table.add_row(car.merk)
        car_table.add_row(car.warna)
        car_table.add_row(f"{int(car.harga_sewa_per_jam):,}/jam")
        car_table.add_row(Panel("Sewa", style="bold white on black", expand=False))
        car_panels.append(Panel(car_table, title=f"Mobil {index}", padding=(1, 2)))

    rows = [car_panels[i:i + 5] for i in range(0, len(car_panels), 5)]
    for row in rows:
        console.print(Columns(row, equal=True, expand=True))