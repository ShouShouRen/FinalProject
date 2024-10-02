import Local from './Local';
import Remote from './Remote';
const SingleDir = () => {
  return (
    <div id='SingleDir' className='flex flex-row justify-center space-x-1 mt-1 h-48'>
      <Local />
      <Remote />
    </div>
  );
};

export default SingleDir;
