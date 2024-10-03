import Local from './Local';
import Remote from './Remote';
const FileList = () => {
  return (
    <div className='flex flex-row w-full h-full gap-2 '>
      <div className='flex-1 overflow-auto'>
        {/* <Local /> */}
        <div className='h-full px-2 py-1 bg-gray-500 border-2 rounded'>Local</div>
      </div>
      <div className='flex-1'>
        <Remote />
      </div>
    </div>
  );
};

export default FileList;
