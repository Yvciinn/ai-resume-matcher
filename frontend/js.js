const addBtn = document.getElementById("add-job-btn");
const jobsContainer = document.getElementById("job-container");
const submitBtn = document.getElementById("submit-btn");
const resumeInput = document.querySelector(".resume_text");
const resultContainer = document.getElementById("result-container");

addBtn.addEventListener("click", () => {
  const newDiv = document.createElement("div");
  newDiv.className = "job_input";
  newDiv.innerHTML = `
    <input type="text" class="job_title" placeholder="Job title" />
    <input type="text" class="job_text" placeholder="Job description" />
  `;
  jobsContainer.insertBefore(newDiv, addBtn);
});

submitBtn.addEventListener("click", async () => {
  const resumeText = resumeInput.value.trim();
  if (!resumeText) {
    resultContainer.innerHTML = "Please enter a resume!";
    return;
  }

  const jobInputs = document.querySelectorAll(".job_input");
  const jobs = [];
  jobInputs.forEach((div) => {
    const title = div.querySelector(".job_title").value.trim();
    const desc = div.querySelector(".job_text").value.trim();
    if (title && desc) {
      jobs.push({ title: title, description: desc });
    }
  });

  if (jobs.length === 0) {
    resultContainer.innerHTML =
      "Please add at least one job title and description!";
    return;
  }

  resultContainer.innerHTML = "<p>⏳ Analyzing your resume against jobs...</p>";

  try {
    const response = await fetch("http://127.0.0.1:8000/match_jobs", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ resume_text: resumeText, jobs: jobs }),
    });

    const data = await response.json();
    displayResults(data.matches);
  } catch (error) {
    console.error(error);
    resultContainer.innerHTML = "Error connecting to server";
  }
});

function displayResults(matches) {
  resultContainer.innerHTML = "<h4>Top Matches</h4>";

  if (!matches || matches.length === 0) {
    resultContainer.innerHTML += "<p>No matches found.</p>";
    return;
  }

  matches.forEach((job) => {
    const p = document.createElement("p");
    p.textContent = `${job.title} → Score: ${job.score.toFixed(2)}`;
    resultContainer.appendChild(p);
  });
}
