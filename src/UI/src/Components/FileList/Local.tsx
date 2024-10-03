import React, { useState } from 'react';
import { Menu, Item, useContextMenu, ItemParams } from 'react-contexify';
import 'react-contexify/ReactContexify.css';

// 文件夾/文件的數據結構
const fileStructure = [
  {
    type: 'folder',
    name: 'Documents',
    children: [
      { type: 'file', name: 'resume.pdf' },
      { type: 'file', name: 'cover_letter.docx' },
    ],
  },
  {
    type: 'folder',
    name: 'Pictures',
    children: [
      { type: 'file', name: 'holiday_photo.jpg' },
      {
        type: 'folder',
        name: 'Travel',
        children: [
          { type: 'file', name: 'paris.jpg' },
          { type: 'file', name: 'tokyo.png' },
        ],
      },
    ],
  },
  { type: 'file', name: 'notes.txt' },
  { type: 'file', name: 'notd.txt' },
];

const MENU_FILE_ID = 'file_menu';
const MENU_FOLDER_ID = 'folder_menu';

const Local = () => {
  const { show: showFileMenu } = useContextMenu({ id: MENU_FILE_ID });
  const { show: showFolderMenu } = useContextMenu({ id: MENU_FOLDER_ID });

  const [currentItem, setCurrentItem] = useState<string | null>(null);
  const [currentType, setCurrentType] = useState<'file' | 'folder' | null>(null);

  // 處理右鍵菜單的顯示邏輯
  const handleContextMenu = (
    event: React.MouseEvent<HTMLDivElement, MouseEvent>,
    type: 'file' | 'folder',
    name: string,
  ) => {
    event.preventDefault();
    setCurrentItem(name); // 設置當前點擊的文件/文件夾名稱
    setCurrentType(type); // 設置當前的類型 (文件 or 文件夾)
    console.log(currentItem);
    // 根據文件/文件夾顯示不同的上下文菜單
    if (type === 'file') {
      showFileMenu({ event, props: { name } });
    } else {
      showFolderMenu({ event, props: { name } });
    }
  };

  // 遞歸渲染文件和文件夾
  const renderFileTree = (structure: any[]) => {
    return structure.map((item) => {
      if (item.type === 'folder') {
        return (
          <div key={item.name} className='ml-4'>
            <div
              className='p-2 m-2 bg-blue-200 border rounded'
              onContextMenu={(event) => handleContextMenu(event, 'folder', item.name)}
            >
              📁 {item.name}
            </div>
            {renderFileTree(item.children)} {/* 遞歸渲染子文件夾和文件 */}
          </div>
        );
      }
      return (
        <div
          key={item.name}
          className='p-2 m-2 bg-white border rounded'
          onContextMenu={(event) => handleContextMenu(event, 'file', item.name)}
        >
          📄 {item.name}
        </div>
      );
    });
  };

  const handleItemClick = ({ id, props }: ItemParams) => {
    if (currentType === 'file') {
      switch (id) {
        case 'upload':
          console.log('Uploading file:', props.name);
          break;
        case 'delete':
          console.log('Deleting file:', props.name);
          break;
        case 'rename':
          console.log('Renaming file:', props.name);
          break;
        default:
          console.log('Unknown action');
      }
    } else if (currentType === 'folder') {
      switch (id) {
        case 'new_file':
          console.log('Creating new file in folder:', props.name);
          break;
        case 'delete_folder':
          console.log('Deleting folder:', props.name);
          break;
        case 'rename_folder':
          console.log('Renaming folder:', props.name);
          break;
        default:
          console.log('Unknown action');
      }
    }
  };

  return (
    <div className='h-full overflow-y-scroll px-2 py-1 bg-gray-500 border-2 rounded'>
      {/* 設置滾動區域 */}
      <div className='overflow-auto min-h-60'>
        {/* 渲染文件夾結構 */}
        {renderFileTree(fileStructure)}
      </div>

      {/* 文件的上下文菜單 */}
      <Menu id={MENU_FILE_ID}>
        <Item id='upload' onClick={handleItemClick}>
          Upload
        </Item>
        <Item id='delete' onClick={handleItemClick}>
          Delete
        </Item>
        <Item id='rename' onClick={handleItemClick}>
          Rename
        </Item>
      </Menu>

      {/* 文件夾的上下文菜單 */}
      <Menu id={MENU_FOLDER_ID}>
        <Item id='new_file' onClick={handleItemClick}>
          New File
        </Item>
        <Item id='delete_folder' onClick={handleItemClick}>
          Delete Folder
        </Item>
        <Item id='rename_folder' onClick={handleItemClick}>
          Rename Folder
        </Item>
      </Menu>
    </div>
  );
};

export default Local;
