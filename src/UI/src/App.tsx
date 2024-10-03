// import { ToolBar, Login, ConnectStatus, FileList, SingleDir, SendStatus } from './Components';
// import MyContextMenu from './Components/MyContextMenu';
// const App = () => {
//   return (
//     <div className='container h-full min-w-full px-6 py-4 bg-gray-700'>
//       <MyContextMenu />
//       <ToolBar />
//       <Login />
//       <ConnectStatus />
//       <FileList />
//       <SingleDir />
//       <SendStatus />
//     </div>
//   );
// };

// export default App;

import { ToolBar, Login, ConnectStatus, FileList, SingleDir, SendStatus } from './Components';

const App = () => {
  return (
    <div className='grid grid-rows-[auto_auto_1fr_auto] h-screen min-w-full bg-gray-700 gap-1 p-2'>
      <div className='space-y-2'>
        <ToolBar />
        <Login />
      </div>
      <div className='h-32'>
        <ConnectStatus />
      </div>

      <div className='grid grid-rows-2 gap-1'>
        <div className='grid grid-cols-1 gap-1'>
          <FileList />
        </div>
        <div className='grid grid-cols-1 gap-1'>
          <SingleDir />
        </div>
      </div>
      <div className='h-32'>
        <SendStatus />
      </div>
    </div>
  );
};

export default App;
