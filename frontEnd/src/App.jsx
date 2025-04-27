import FileUploader from './components/FileUploader';
import './App.css';
import SplineBackground from './components/SplineBackground';

function App() {
  return (
    <div>
      <div className="spline-background">
        <SplineBackground />
      </div>
      <div className="page-wrapper">
        <h1 className="Heading">Resume Grader</h1>
        <div className="main-content">
          <FileUploader />
        </div>
      </div>
    </div>
  );
}

export default App;
