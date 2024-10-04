import { ToolBar, Login, ConnectStatus, FileList, SendStatus } from '@components';

const App = () => {
  return (
    <div className='grid grid-rows-[auto_auto_2fr_auto] h-screen min-w-full bg-gray-700 gap-1 p-2'>
      <div>
        <ToolBar />
        <Login />
      </div>
      <div className='h-28'>
        <ConnectStatus />
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
