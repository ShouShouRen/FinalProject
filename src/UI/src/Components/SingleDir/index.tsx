import Local from './Local';
import Remote from './Remote';
const SingleDir = () => {
  return (
    <div className='flex flex-row gap-2 h-[25vh]'>
      <div className='flex-1'>
        <Local />
      </div>
      <div className='flex-1'>
        <Remote />
      </div>
    </div>
  );
};

export default SingleDir;
