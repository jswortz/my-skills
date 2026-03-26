const { chromium } = require('playwright');

const TARGET_URL = 'https://vertexaisearch.cloud.google.com/home/cid/ed4a91ac-75a2-4f60-b343-1f03b7d22e98/';
const SCREENSHOT_DIR = '/usr/local/google/home/jwortz/zghost/demo_screenshots';

(async () => {
  // Launch with user's Chrome profile for Google Cloud auth — headless since no X server
  const browser = await chromium.launchPersistentContext(
    '/usr/local/google/home/jwortz/.config/google-chrome/Default',
    {
      headless: true,
      channel: 'chrome',
      viewport: { width: 1920, height: 1080 },
      args: [
        '--disable-blink-features=AutomationControlled',
        '--no-first-run',
        '--no-default-browser-check',
        '--no-sandbox',
      ],
      ignoreDefaultArgs: ['--enable-automation'],
    }
  );

  const page = await browser.newPage();

  try {
    console.log('Navigating to Gemini Enterprise...');
    await page.goto(TARGET_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(5000);

    console.log('Page title:', await page.title());
    console.log('Current URL:', page.url());

    // Take landing page screenshot
    await page.screenshot({
      path: `${SCREENSHOT_DIR}/01_gemini_enterprise_landing.png`,
      fullPage: true,
    });
    console.log('Screenshot 1: Landing page saved');

    // Wait for dynamic content
    await page.waitForTimeout(3000);

    await page.screenshot({
      path: `${SCREENSHOT_DIR}/02_gemini_enterprise_loaded.png`,
      fullPage: true,
    });
    console.log('Screenshot 2: Loaded page saved');

    // Viewport-only screenshot
    await page.screenshot({
      path: `${SCREENSHOT_DIR}/03_gemini_enterprise_viewport.png`,
      fullPage: false,
    });
    console.log('Screenshot 3: Viewport saved');

    console.log('All screenshots saved to:', SCREENSHOT_DIR);
  } catch (error) {
    console.error('Error:', error.message);
    await page.screenshot({
      path: `${SCREENSHOT_DIR}/error_screenshot.png`,
      fullPage: true,
    });
  } finally {
    await browser.close();
  }
})();
