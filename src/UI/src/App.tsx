import { ToolBar, Login, ConnectStatus, FileList, SingleDir, SendStatus } from './Components';
const App = () => {
  return (
    <div className='container min-w-full min-h-screen px-6 py-4 bg-gray-700'>
      <ToolBar />
      <Login />
      <ConnectStatus />
      <FileList />
      <SingleDir />
      <SendStatus />
    </div>
  );
};

export default App;
