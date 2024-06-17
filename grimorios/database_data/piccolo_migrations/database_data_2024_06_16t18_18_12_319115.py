from piccolo.apps.migrations.auto.migration_manager import MigrationManager

from database.tables import EstatusTable, GrimorioTable


ID = "2024-06-16T18:18:12:319115"
VERSION = "1.11.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    async def run():
        print(f"running {ID}")

        await GrimorioTable.insert(GrimorioTable(rareza = 35, nombre = "Trébol de 1 hoja"))
        await GrimorioTable.insert(GrimorioTable(rareza = 25, nombre = "Trébol de 2 hojas"))
        await GrimorioTable.insert(GrimorioTable(rareza = 20, nombre = "Trébol de 3 hojas"))
        await GrimorioTable.insert(GrimorioTable(rareza = 15, nombre = "Trébol de 4 hojas"))
        await GrimorioTable.insert(GrimorioTable(rareza = 5, nombre = "Trébol de 5 hojas"))

        await EstatusTable.insert(EstatusTable(estatus = "Pendiente"))
        await EstatusTable.insert(EstatusTable(estatus = "Aceptada"))
        await EstatusTable.insert(EstatusTable(estatus = "Rechazada"))

    manager.add_raw(run)

    return manager
