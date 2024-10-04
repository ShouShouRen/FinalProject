import Local from './Local';
import Remote from './Remote';
const FileList = () => {
  return (
    <div className='flex flex-row w-full h-full gap-2 '>
      <div className='flex-1'>
        <Local />
      </div>
      <div className='flex-1'>
        <Remote />
      </div>
    </div>
  );
};

export default FileList;
