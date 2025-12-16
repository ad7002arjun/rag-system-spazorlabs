const API_BASE = "http://127.0.0.1:8000";

async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const status = document.getElementById("uploadStatus");

  if (!fileInput.files.length) {
    status.textContent = "❌ Please select a file";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  status.textContent = "⏳ Uploading and indexing document...";

  try {
    const res = await fetch(`${API_BASE}/upload`, {
      method: "POST",
      body: formData
    });

    if (!res.ok) throw new Error();

    status.textContent = "✅ Document uploaded & indexed successfully!";
  } catch {
    status.textContent = "❌ Upload failed";
  }
}

async function askQuestion() {
  const question = document.getElementById("questionInput").value;
  const answerBox = document.getElementById("answerBox");

  if (!question.trim()) {
    answerBox.textContent = "❌ Please enter a question";
    return;
  }

  answerBox.textContent = "🧠 Thinking...";

  try {
    const res = await fetch(`${API_BASE}/ask`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    answerBox.textContent = data.answer || "No answer found.";
  } catch {
    answerBox.textContent = "❌ Error getting answer";
  }
}

