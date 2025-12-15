import { useState } from 'react';
import { WelcomeScreen } from './components/WelcomeScreen';
import { HomeDashboard } from './components/HomeDashboard';
import { CitizenRiskScreen } from './components/CitizenRiskScreen';
import { AccidentDetectionScreen } from './components/AccidentDetectionScreen';
import { ResultScreen } from './components/ResultScreen';

export type Screen = 'welcome' | 'home' | 'citizen-risk' | 'accident-detection' | 'result';
export type ResultType = {
  type: 'citizen-risk' | 'accident-detection';
  level?: 'low' | 'medium' | 'high';
  hasAccident?: boolean;
  data?: any;
};

export default function App() {
  const [currentScreen, setCurrentScreen] = useState<Screen>('welcome');
  const [result, setResult] = useState<ResultType | null>(null);

  const navigateTo = (screen: Screen) => {
    setCurrentScreen(screen);
  };

  const showResult = (resultData: ResultType) => {
    setResult(resultData);
    setCurrentScreen('result');
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-green-50">
      {currentScreen === 'welcome' && (
        <WelcomeScreen onGetStarted={() => navigateTo('home')} />
      )}
      {currentScreen === 'home' && (
        <HomeDashboard onNavigate={navigateTo} currentTab="home" />
      )}
      {currentScreen === 'citizen-risk' && (
        <CitizenRiskScreen onBack={() => navigateTo('home')} onResult={showResult} />
      )}
      {currentScreen === 'accident-detection' && (
        <AccidentDetectionScreen onBack={() => navigateTo('home')} onResult={showResult} />
      )}
      {currentScreen === 'result' && result && (
        <ResultScreen result={result} onBack={() => navigateTo('home')} />
      )}
    </div>
  );
}
