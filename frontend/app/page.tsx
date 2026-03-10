'use client';

import { useState, useEffect } from 'react';

export default function Home() {
  const [clues, setClues] = useState<string[]>([]);
  const [countryId, setCountryId] = useState('');
  const [guess, setGuess] = useState('');
  const [result, setResult] = useState('');
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  const [correct, setCorrect] = useState(0);
  const [wrong, setWrong] = useState(0);
  const [finished, setFinished] = useState(false);

  const fetchCountry = async () => {
    setResult('');
    setGuess('');
    setIsCorrect(null);
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/country`);
    const data = await res.json();
    setClues(data.clues);
    setCountryId(data.id);
  };

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/reset`, { method: 'POST' });
    fetchCountry();
  }, []);

  const submitGuess = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/guess`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ guess, id: countryId }),
    });
    const data = await res.json();
    setResult(data.message);
    setIsCorrect(data.correct);
    if (data.correct) setCorrect(c => c + 1);
    else setWrong(w => w + 1);
  };

  const playAgain = () => {
    setCorrect(0);
    setWrong(0);
    setFinished(false);
    fetchCountry();
  };

  if (finished) {
    const total = correct + wrong;
    const percentage = total > 0 ? Math.round((correct / total) * 100) : 0;
    return (
      <main className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="bg-white rounded-2xl shadow-md p-10 w-full max-w-md text-center">
          <h1 className="text-3xl font-bold text-gray-800 mb-6">🏁 Game Over!</h1>
          <div className="space-y-3 mb-8">
            <p className="text-lg">✅ Correct: <span className="font-bold text-green-600">{correct}</span></p>
            <p className="text-lg">❌ Wrong: <span className="font-bold text-red-500">{wrong}</span></p>
            <p className="text-lg">🎯 Score: <span className="font-bold text-blue-500">{percentage}%</span></p>
          </div>
          <button
            onClick={playAgain}
            className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 rounded-xl transition"
          >
            Play Again
          </button>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="bg-white rounded-2xl shadow-md p-10 w-full max-w-md">
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-2">
          🌍 Guess The Country
        </h1>
        <p className="text-center text-gray-400 mb-8">Use the clues to guess the country</p>

        <div className="space-y-3 mb-8">
          {clues.map((clue, i) => (
            <div key={i} className="flex items-start gap-3 bg-blue-50 rounded-xl p-4">
              <span className="text-blue-500 font-bold">#{i + 1}</span>
              <p className="text-gray-700">{clue}</p>
            </div>
          ))}
        </div>

        <input
          type="text"
          value={guess}
          onChange={(e) => setGuess(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && submitGuess()}
          placeholder="Type your answer..."
          className="w-full border border-gray-200 rounded-xl px-4 py-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-300 mb-3"
        />

        {!result && (
          <button
            onClick={submitGuess}
            className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 rounded-xl transition mb-3"
          >
            Submit Guess
          </button>
        )}

        {result && (
          <div className={`text-center font-semibold py-3 rounded-xl mb-3 ${isCorrect ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
            {result}
          </div>
        )}

        <div className="flex gap-2">
          <button
            onClick={() => setFinished(true)}
            className="flex-1 border border-gray-200 hover:bg-gray-50 text-gray-500 py-3 rounded-xl transition"
          >
            Finish 🏁
          </button>
          <button
            onClick={fetchCountry}
            className="flex-1 border border-gray-200 hover:bg-gray-50 text-gray-500 py-3 rounded-xl transition"
          >
            Next Country →
          </button>
        </div>

      </div>
    </main>
  );
}