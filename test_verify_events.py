from playwright.sync_api import sync_playwright
import subprocess
import time

def run_cuj(page):
    page.goto("http://localhost:8088/index.html")
    page.wait_for_timeout(1000)

    # Clear localStorage so defaultEvents rendered afresh
    page.evaluate("localStorage.clear()")
    page.reload()
    page.wait_for_timeout(1000)

    # Scroll to events section
    events_section = page.locator("#events")
    events_section.scroll_into_view_if_needed()
    page.wait_for_timeout(1000)

    # Take screenshot of events section
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    # Start local http server on port 8088
    server_process = subprocess.Popen(["python3", "-m", "http.server", "8088"])
    time.sleep(1)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                record_video_dir="/home/jules/verification/videos"
            )
            page = context.new_page()
            try:
                run_cuj(page)
            finally:
                context.close()
                browser.close()
    finally:
        server_process.terminate()
