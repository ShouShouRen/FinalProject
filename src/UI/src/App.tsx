import { ToolBar, Login, ConnectStatus, FileList, SendStatus } from '@components';
import { useState } from 'react';

const App = () => {
  const [message, setMessage] = useState<string>('');
  return (
    <div className='grid grid-rows-[auto_auto_2fr_auto] h-screen min-w-full bg-gray-700 gap-1 p-2'>
      <div>
        <ToolBar />
        <Login setMessage={setMessage} />
      </div>
      <div className='h-28'>
        <ConnectStatus message={message} />
      </div>

      <div className='grid grid-rows-1 gap-1'>
        <div className='grid grid-cols-1 gap-1'>
          <FileList />
        </div>
      </div>
      <div className='h-28'>
        <SendStatus />
      </div>
    </div>
  );
};

export default App;
