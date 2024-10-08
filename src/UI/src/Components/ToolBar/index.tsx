import {
  RiInformation2Fill,
  RiIndentIncrease,
  RiIndentDecrease,
  RiArrowLeftRightFill,
  RiServerFill,
} from 'react-icons/ri';
import { TfiReload } from 'react-icons/tfi';
import { GiCancel } from 'react-icons/gi';
import { TbPlugConnected, TbPlugConnectedX } from 'react-icons/tb';
import { useEffect, useState } from 'react';
import { Button, Flex, Input, List, Modal, Space, Typography } from 'antd';
const { Text } = Typography;
type DataItem = { name: string; host: string; user: string; password: string; port: string };
const ToolBar = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [dataList, setDataList] = useState(() => {
    const savedData = localStorage.getItem('dataList');
    return savedData ? JSON.parse(savedData) : [];
  });
  const [host, setHost] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [port, setPort] = useState('');
  const [user, setUser] = useState('');
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  useEffect(() => {
    localStorage.setItem('dataList', JSON.stringify(dataList));
  }, [dataList]);

  const handleAdd = () => {
    if (host.trim() && user.trim() && password.trim() && port.trim()) {
      const isEditing = dataList.some((item: DataItem) => item.host === host);
      if (isEditing) {
        setDataList(
          dataList.map((item: DataItem) =>
            item.name === name ? { host, user, password, port } : item,
          ),
        );
      } else {
        setDataList([...dataList, { name: name.trim(), host: host.trim(), user, password, port }]);
      }
      setHost('');
      setUser('');
      setPassword('');
      setPort('');
      setName('');
    }
  };
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    const title = e.currentTarget.getAttribute('title');
    console.log(`Button clicked: ${title}`);
  };

  const handleEdit = (item: DataItem) => {
    setHost(item.host);
    setName(item.name);
    setUser(item.user);
    setPassword(item.password);
    setPort(item.port);
    setIsEditing(true);
    setIsModalVisible(true);
  };
  const handleConnect = (item: DataItem) => {
    console.log(`Connecting to ${item.host}`);
  };
  const handleDelete = (item: DataItem) => {
    setDataList(dataList.filter((i: DataItem) => i.host !== item.host));
  };
  const onClose = () => {
    setHost('');
    setUser('');
    setPassword('');
    setPort('');
    setName('');
    setIsEditing(false);
    setIsModalVisible(false);
  };

  return (
    <div className='flex flex-row items-center space-x-5 bg-gray-500 border border-white'>
      <div className='flex items-center'>
        <button title='站台管理員' onClick={() => setIsModalVisible(true)}>
          <RiServerFill className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#87A2FF' />
        </button>
        <Modal
          title='保存資料管理'
          open={isModalVisible}
          onCancel={onClose}
          cancelText='關閉'
          okText={name ? '保存' : '新增'}
          onOk={handleAdd}
          destroyOnClose={true}
        >
          <div className='flex flex-row w-full'>
            <div className='w-1/2 text-center flex1 h-[250px] overflow-auto'>
              <List
                dataSource={dataList}
                header={<div>站台列表</div>}
                renderItem={(item: DataItem, index) => (
                  <List.Item
                    key={index}
                    onClick={() => handleEdit(item)}
                    className='text-lg cursor-pointer w-full'
                  >
                    <p>{`${item.name}`}</p>
                    <div>
                      <Button
                        className='ml-2'
                        onClick={(e) => {
                          e.stopPropagation();
                          handleDelete(item);
                        }}
                      >
                        刪除
                      </Button>
                      <Button
                        className='ml-2'
                        onClick={(e) => {
                          e.stopPropagation();
                          handleConnect(item);
                        }}
                      >
                        連線
                      </Button>
                    </div>
                  </List.Item>
                )}
              />
            </div>
            <div className='w-1/2 text-center flex1'>
              <Space direction='vertical'>
                <Input
                  placeholder='名稱'
                  value={name}
                  disabled={isEditing}
                  onChange={(e) => setName(e.target.value)}
                />

                <Input
                  placeholder='主機地址'
                  value={host}
                  defaultValue='127.0.0.1'
                  onChange={(e) => setHost(e.target.value)}
                />
                <Input
                  placeholder='使用者帳號'
                  value={user}
                  onChange={(e) => setUser(e.target.value)}
                />
                <Input.Password
                  placeholder='使用者密碼'
                  visibilityToggle={{
                    visible: passwordVisible,
                    onVisibleChange: setPasswordVisible,
                  }}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <Input
                  placeholder='連接埠'
                  value={port}
                  defaultValue='50051'
                  onChange={(e) => setPort(e.target.value)}
                />
              </Space>
            </div>
          </div>
        </Modal>
      </div>
      <div className='flex items-center gap-1'>
        <button title='連線紀錄' onClick={handleClick}>
          <RiInformation2Fill
            className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16'
            color='#ffc800'
          />
        </button>
        <button title='切換本地目錄樹' onClick={handleClick}>
          <RiIndentDecrease className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#7acf6a' />
        </button>
        <button title='切換遠端目錄樹' onClick={handleClick}>
          <RiIndentIncrease className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#87A2FF' />
        </button>
        <button title='檔案傳輸過程' onClick={handleClick}>
          <RiArrowLeftRightFill
            className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16'
            color='#5ba4a4'
          />
        </button>
      </div>
      <div className='flex items-center'>
        <button title='重新整理檔案及資料夾' onClick={handleClick}>
          <TfiReload className='h-9 w-9 lg:w-16 lg:h-16 md:w-12 md:h-12' color='#99ff99' />
        </button>
        <button title='取消檔案動作' className='ml-2 lg:ml-4 md:ml-3' onClick={handleClick}>
          <GiCancel className='w-10 h-10 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#cc0000' />
        </button>
        <button title='連接伺服器' className='ml-1 md:ml-2' onClick={handleClick}>
          <TbPlugConnected className='w-10 h-10 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#99ff33' />
        </button>
        <button title='中斷伺服器' className='-ml-1 md:-ml-2' onClick={handleClick}>
          <TbPlugConnectedX className='w-10 h-10 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#ff6600' />
        </button>
      </div>
    </div>
  );
};

export default ToolBar;
