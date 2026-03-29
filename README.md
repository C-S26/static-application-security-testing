# Static Application Security Testing (SAST) – Hands-on Analysis

## Overview

This repository demonstrates **Static Application Security Testing (SAST)** techniques used to identify security vulnerabilities in source code **without executing the application**.

The goal of this project is to analyze code for common security flaws and understand how vulnerabilities can be detected early in the development lifecycle.

---

## Objectives

* Understand principles of static code analysis
* Identify common security vulnerabilities in source code
* Perform manual and tool-based static testing
* Document findings and security risks

---

## Tools & Techniques

* Manual Code Review
* Pattern-based vulnerability detection
* (Optional – add if used) Semgrep / Bandit / ESLint security plugins

---

## Test Cases & Analysis

### 1. Input Validation Issues

* Missing validation on user input
* Potential injection risks

### 2. Hardcoded Credentials

* Sensitive data stored directly in source code
* Security risk for exposure

### 3. Improper Error Handling

* Information leakage through error messages

### 4. Insecure Coding Practices

* Lack of sanitization
* Unsafe handling of user-controlled data

---

## Findings

| Vulnerability Type     | Description                    | Impact |
| ---------------------- | ------------------------------ | ------ |
| Input Validation Flaw  | Unchecked user input           | High   |
| Hardcoded Secrets      | Credentials exposed in code    | High   |
| Error Handling Issues  | Sensitive info leakage         | Medium |
| Insecure Data Handling | Unsafe processing of user data | High   |

---

## Key Learnings

* Static testing helps identify vulnerabilities **before deployment**
* Early detection reduces risk and cost of fixing issues
* Secure coding practices are essential for application security

---

## Future Improvements

* Integrate automated SAST tools (Semgrep, Bandit)
* Expand test cases with real-world vulnerable code samples
* Compare results between different static analysis tools

---

## Conclusion

This project demonstrates how static analysis can be used to proactively identify security issues and improve overall application security posture.

## Key Concepts Covered
- **SAST (Static Analysis)**: Reviewing code for flaws without actually running it.
- **Patch Management**: The lifecycle of identifying and deploying code updates to mitigate risks.
- **Secure Authentication**: Moving away from hardcoded secrets toward secure storage methods.

