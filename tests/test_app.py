from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_homepage_loads_correctly_when_logged_out(page, test_web_address, db_connection):
    db_connection.seed("seeds/MBnB.sql")
    page.goto(f"http://{test_web_address}/")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("🏘️ MBnB")

    space_headers = page.locator(".space-header")
    expect(space_headers).to_have_text([
        "Cottage",
        "Villa",
        "Alpine lodge",
        "Studio Apartment",
        "Tent"
    ])

    space_descriptions = page.locator(".space-description")
    expect(space_descriptions).to_have_text([
        "A nice cottage",
        "A mediterranean villa with a sea view",
        "A cosy ski lodge with wood-burning fire",
        "A cool apartment in the centre of the bustling city",
        "A 5 metre, cotton canvas bell tent which can comfortably accommodate up to 4 people with any combination of single beds or double bed, duvets and pillows with linen, rugs, blankets, cushions, lighting, side tables, seating and plants."
    ])

    space_prices = page.locator(".space-price")
    expect(space_prices).to_have_text([
        "From £27 per night!",
        "From £70 per night!",
        "From £95 per night!",
        "From £102 per night!",
        "From £50 per night!"
    ])
