import Local from './Local';
import Remote from './Remote';
const FileList = () => {
  return (
    <div id='FileList' className='flex flex-row justify-center space-x-3'>
      <Local />
      <Remote />
    </div>
  );
};

export default FileList;
