from dagster import load_assets_from_package_module, repository

from jaffle import assets


@repository
def jaffle():
    return [load_assets_from_package_module(assets)]
