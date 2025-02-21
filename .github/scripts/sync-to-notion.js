const { Client } = require('@notionhq/client');
const fs = require('fs');
const path = require('path');

const notion = new Client({
  auth: process.env.NOTION_KEY,
});

async function uploadToNotion(filePath, content) {
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
                content: path.basename(filePath),
              },
            },
          ],
        },
        Path: {
          rich_text: [
            {
              text: {
                content: filePath,
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
                  content: content,
                },
              },
            ],
          },
        },
      ],
    });
    console.log(`Successfully uploaded ${filePath} to Notion`);
  } catch (error) {
    console.error(`Error uploading ${filePath}:`, error);
  }
}

async function main() {
  const files = process.env.GITHUB_EVENT_PATH
    ? require(process.env.GITHUB_EVENT_PATH)
    : { commits: [] };

  for (const commit of files.commits) {
    const javaFiles = commit.added
      .concat(commit.modified)
      .filter((file) => file.endsWith('.java'));

    for (const file of javaFiles) {
      const content = fs.readFileSync(file, 'utf8');
      await uploadToNotion(file, content);
    }
  }
}

main().catch(console.error);
