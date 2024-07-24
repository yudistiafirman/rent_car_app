from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from helpers.utils.formatter import format_date

def display_payment_details(reservation_details):
    console = Console()

    detail_table = Table.grid(padding=(0, 1))
    detail_table.add_column(justify="left", width=20)
    detail_table.add_column(justify="left", width=30)

    details = {
        "Nama Mobil": reservation_details["car"]["name"],
        "Transmisi": reservation_details["car"]["jenis_transmisi"],
        "Merk": reservation_details["car"]["merk"],
        "Warna": reservation_details["car"]["warna"],
        "Plat No": reservation_details["car"]["plat_nomor"],
        "Tanggal awal sewa": f"{format_date(reservation_details['tanggal_mulai'])} {reservation_details['jam_mulai']}",
        "Tanggal akhir sewa": f"{format_date(reservation_details['tanggal_selesai'])} {reservation_details['jam_selesai']}",
        "Durasi sewa": f"{int(reservation_details['durasi_sewa'])} jam",
        "Harga sewa / jam": f"Rp.{int(reservation_details['car']['harga_sewa']):,}",
        "Total Harga": f"Rp.{int(reservation_details['total_biaya']):,}"
    }

    for key, value in details.items():
        detail_table.add_row(key, value)

    detail_panel = Panel.fit(detail_table, title="Detail Pembayaran", padding=(1, 2))

    console.print(detail_panel)