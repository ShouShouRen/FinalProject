import React, { useEffect, useRef, useState } from 'react';
import { List, Space } from 'antd';

interface ConnectStatusProps {
  message: string;
}

const ConnectStatus: React.FC<ConnectStatusProps> = ({ message }) => {
  const [messages, setMessages] = useState<string[]>([]);
  const listRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setMessages((prevMessages) => [...prevMessages, message]);
  }, [message]);

  useEffect(() => {
    if (listRef.current) {
      listRef.current.scrollTop = listRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div
      ref={listRef}
      className='w-full h-full p-2 overflow-auto bg-gray-500 border'
      style={{ maxHeight: '400px' }}
    >
      <Space direction='vertical'>
        <List
          dataSource={messages}
          renderItem={(msg, index) => (
            <List.Item key={index} style={{ paddingTop: '2px', paddingBottom: '2px' }}>
              <div className='flex items-center w-full h-full px-2 text-white'>{msg}</div>
            </List.Item>
          )}
        />
      </Space>
    </div>
  );
};

export default ConnectStatus;
