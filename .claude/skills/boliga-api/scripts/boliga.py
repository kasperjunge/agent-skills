#!/usr/bin/env python3
"""
Boliga API client - Danish real estate data as pandas DataFrames.

Usage:
    from boliga import get_properties, Municipality, PropertyType

    df = get_properties(municipality=Municipality.ROSKILDE, property_type=PropertyType.HOUSE)
    avg_sqm_price = df['sqm_price'].mean()
"""

import requests
import pandas as pd
from enum import IntEnum
from typing import Optional

# Base URLs
BASE_URL = "https://api.boliga.dk/api/v2"
BASE_URL2 = "https://api2.boliga.dk"


class Municipality(IntEnum):
    """Danish municipality codes."""
    COPENHAGEN = 101
    FREDERIKSBERG = 147
    BALLERUP = 151
    BRONDBY = 153
    DRAGOR = 155
    GENTOFTE = 157
    GLADSAXE = 159
    GLOSTRUP = 161
    HERLEV = 163
    ALBERTSLUND = 165
    HVIDOVRE = 167
    TODAY_TAASTRUP = 169
    LYNGBY_TAARBAEK = 173
    RODOVRE = 175
    ISHOJ = 183
    TAARNBY = 185
    VALLENSBAEK = 187
    FURESO = 190
    ROSKILDE = 265
    AARHUS = 751
    ODENSE = 461
    HORSENS = 615
    GULDBORGSUND = 376


class PropertyType(IntEnum):
    """Property type codes."""
    VILLA = 1          # Villa/House
    TERRACED = 2       # Rækkehus/Terraced house
    APARTMENT = 3      # Ejerlejlighed/Apartment
    HOLIDAY = 4        # Fritidshus/Holiday home
    COOPERATIVE = 5    # Andelsbolig/Cooperative
    FARM = 6           # Landejendom/Farm
    HOBBY_FARM = 7     # Hobbylandbrug
    PLOT = 8           # Grund/Plot
    COMMERCIAL = 9     # Erhverv/Business
    OTHER = 10         # Andet/Other


class SortOrder:
    """Sort options for property search."""
    PRICE_ASC = "price-a"
    PRICE_DESC = "price-d"
    SQM_PRICE_ASC = "sqmPrice-a"
    SQM_PRICE_DESC = "sqmPrice-d"
    DAYS_FOR_SALE_ASC = "daysForSale-a"
    DAYS_FOR_SALE_DESC = "daysForSale-d"
    VIEWS_DESC = "views-d"
    ZIP_ASC = "zipCode-a"


def get_properties(
    municipality: Optional[int] = None,
    zip_codes: Optional[str] = None,
    property_type: Optional[int] = None,
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    rooms_min: Optional[int] = None,
    rooms_max: Optional[int] = None,
    size_min: Optional[int] = None,
    size_max: Optional[int] = None,
    build_year_min: Optional[int] = None,
    build_year_max: Optional[int] = None,
    sort: Optional[str] = None,
    page_size: int = 50,
    page: int = 1,
) -> pd.DataFrame:
    """
    Search properties for sale on Boliga.

    Args:
        municipality: Municipality code (use Municipality enum)
        zip_codes: Comma-separated zip codes (e.g., "4000,4990")
        property_type: Property type code (use PropertyType enum)
        price_min: Minimum price in DKK
        price_max: Maximum price in DKK
        rooms_min: Minimum number of rooms
        rooms_max: Maximum number of rooms
        size_min: Minimum size in m2
        size_max: Maximum size in m2
        build_year_min: Minimum build year
        build_year_max: Maximum build year
        sort: Sort order (use SortOrder class)
        page_size: Results per page (max 50)
        page: Page number

    Returns:
        DataFrame with columns: id, address, city, zip_code, price, sqm_price,
        size, rooms, build_year, property_type, days_for_sale, lat, lon, etc.
    """
    params = {"pageSize": page_size, "page": page}

    if municipality:
        params["municipality"] = municipality
    if zip_codes:
        params["zipCodes"] = zip_codes
    if property_type:
        params["propertyType"] = property_type
    if price_min:
        params["priceMin"] = price_min
    if price_max:
        params["priceMax"] = price_max
    if rooms_min:
        params["roomsMin"] = rooms_min
    if rooms_max:
        params["roomsMax"] = rooms_max
    if size_min:
        params["sizeMin"] = size_min
    if size_max:
        params["sizeMax"] = size_max
    if build_year_min:
        params["buildYearMin"] = build_year_min
    if build_year_max:
        params["buildYearMax"] = build_year_max
    if sort:
        params["sort"] = sort

    response = requests.get(f"{BASE_URL}/search/results", params=params)
    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        return pd.DataFrame()

    df = pd.DataFrame(data["results"])

    # Rename columns to snake_case
    column_map = {
        "squaremeterPrice": "sqm_price",
        "propertyType": "property_type",
        "buildYear": "build_year",
        "daysForSale": "days_for_sale",
        "zipCode": "zip_code",
        "lotSize": "lot_size",
        "basementSize": "basement_size",
        "energyClass": "energy_class",
        "latitude": "lat",
        "longitude": "lon",
    }
    df = df.rename(columns=column_map)

    # Select most useful columns
    cols = [
        "id", "street", "city", "zip_code", "price", "sqm_price", "size",
        "rooms", "build_year", "property_type", "days_for_sale", "lot_size",
        "energy_class", "lat", "lon", "views"
    ]
    available_cols = [c for c in cols if c in df.columns]

    return df[available_cols]


def get_sold_properties(
    municipality: Optional[int] = None,
    property_type: Optional[int] = None,
    rooms_min: Optional[int] = None,
    rooms_max: Optional[int] = None,
    size_min: Optional[int] = None,
    size_max: Optional[int] = None,
    page_size: int = 50,
    page: int = 1,
) -> pd.DataFrame:
    """
    Search historically sold properties.

    Returns:
        DataFrame with sold property data.
    """
    params = {"pageSize": page_size, "page": page, "searchTab": 1}

    if municipality:
        params["municipality"] = municipality
    if property_type:
        params["propertyType"] = property_type
    if rooms_min:
        params["roomsMin"] = rooms_min
    if rooms_max:
        params["roomsMax"] = rooms_max
    if size_min:
        params["sizeMin"] = size_min
    if size_max:
        params["sizeMax"] = size_max

    response = requests.get(f"{BASE_URL}/nfs/search/results", params=params)
    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        return pd.DataFrame()

    return pd.DataFrame(data["results"])


def get_estate_details(estate_id: int) -> dict:
    """
    Get detailed information about a specific property.

    Args:
        estate_id: The Boliga estate ID

    Returns:
        Dictionary with sqm_price, discount, popularity, days_for_sale data.
    """
    details = {}

    endpoints = ["sqmprice", "discount", "popularity", "daysforsale"]
    for endpoint in endpoints:
        try:
            response = requests.get(f"{BASE_URL}/estate/{estate_id}/{endpoint}")
            if response.ok:
                details[endpoint] = response.json()
        except Exception:
            pass

    return details


def get_property_history(estate_id: int, extended: bool = True) -> pd.DataFrame:
    """
    Get historical data for a specific property.

    Args:
        estate_id: The Boliga estate ID
        extended: Include extended history

    Returns:
        DataFrame with property history.
    """
    params = {"extended": "true"} if extended else {}
    response = requests.get(
        f"{BASE_URL}/estate/{estate_id}/improvedhistory",
        params=params
    )
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list):
        return pd.DataFrame(data)
    return pd.DataFrame([data]) if data else pd.DataFrame()


def get_market_statistics() -> dict:
    """
    Get national market statistics.

    Returns:
        Dictionary with price development and market overview.
    """
    stats = {}

    try:
        response = requests.get(f"{BASE_URL}/statistics/salespricedevelopment")
        if response.ok:
            stats["price_development"] = response.json()
    except Exception:
        pass

    try:
        response = requests.get(f"{BASE_URL}/frontpage/stats")
        if response.ok:
            stats["overview"] = response.json()
    except Exception:
        pass

    return stats


def search_location(query: str, limit: int = 10) -> pd.DataFrame:
    """
    Search for locations (autocomplete).

    Args:
        query: Search text (city, zip code, or area name)
        limit: Max results

    Returns:
        DataFrame with location suggestions.
    """
    params = {"q": query, "areaLimit": limit, "addressLimit": limit}
    response = requests.get(f"{BASE_URL}/location/suggestions", params=params)
    response.raise_for_status()
    data = response.json()

    results = data.get("areas", []) + data.get("addresses", [])
    return pd.DataFrame(results) if results else pd.DataFrame()


def get_new_construction(municipality: Optional[int] = None) -> pd.DataFrame:
    """
    Get new construction projects.

    Args:
        municipality: Municipality code filter

    Returns:
        DataFrame with new construction projects.
    """
    params = {}
    if municipality:
        params["municipalityCode"] = municipality

    response = requests.get(f"{BASE_URL2}/newhomes/v1/projects", params=params)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list):
        return pd.DataFrame(data)
    return pd.DataFrame(data.get("projects", [])) if data else pd.DataFrame()


if __name__ == "__main__":
    # Example usage
    df = get_properties(
        municipality=Municipality.ROSKILDE,
        property_type=PropertyType.TERRACED
    )
    print(f"Found {len(df)} terraced houses in Roskilde")
    print(f"Average price per m2: {df['sqm_price'].mean():,.0f} DKK")
