import Local from './Local';
import Remote from './Remote';
const FileList = () => {
  return (
    <div className='flex flex-row gap-2 h-[25vh]'>
      <div className='w-1/2 h-full'>
        <Local />
      </div>
      <div className='w-1/2 h-full'>
        <Remote />
      </div>
    </div>
  );
};

export default FileList;
