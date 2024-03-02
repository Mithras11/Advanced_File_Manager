import click

from app.utils import organizer, scanner


@click.group()
def cli() -> None:
    pass


cli.add_command(scanner.scan_files)
cli.add_command(scanner.scan_subdirs)
cli.add_command(scanner.build_catalog)
cli.add_command(scanner.build_catalog_recursively)
cli.add_command(scanner.build_tree)
cli.add_command(scanner.build_pretty_tree)
cli.add_command(scanner.search_by_name)
cli.add_command(scanner.search_by_name_recursively)

cli.add_command(organizer.organize_files)
cli.add_command(organizer.organize_files_recursively)

cli.add_command(organizer.handle_duplicate_files)
