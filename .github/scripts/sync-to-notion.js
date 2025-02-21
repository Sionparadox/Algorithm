const { Client } = require('@notionhq/client');

const notion = new Client({
  auth: process.env.NOTION_KEY,
});

async function uploadToNotion(code, title) {
  try {
    await notion.pages.create({
      parent: {
        database_id: process.env.NOTION_DATABASE_ID,
      },
      properties: {
        Name: {
          title: [
            {
              text: {
                content: title,
              },
            },
          ],
        },
      },
      children: [
        {
          object: 'block',
          type: 'code',
          code: {
            language: 'java',
            rich_text: [
              {
                text: {
                  content: code,
                },
              },
            ],
          },
        },
      ],
    });
    console.log(`Successfully uploaded ${title} to Notion`);
  } catch (error) {
    console.error(`Error uploading ${title}:`, error);
  }
}

async function main() {
  const code = process.env.CODE;
  const title = process.env.TITLE;

  if (!code || !title) {
    console.error('CODE or TITLE environment variable is missing');
    process.exit(1);
  }

  await uploadToNotion(code, title);
}

main().catch(console.error);
