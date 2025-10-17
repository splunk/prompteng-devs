# Activity 3.3 Solution: Template Customization Challenge

## ✅ What Makes This Solution Follow Best Practices

### 1. Performance-Specific Role and Context

```python
"You are a Senior Performance Engineer specializing in database optimization."
```

```xml
<context>
Performance Requirements: Must handle users with 1000+ posts efficiently
</context>
```

**Why this matters:**
- Role matches the specific focus area (performance, not general review)
- Context includes scale requirements (1000+ posts) - critical for performance analysis
- Sets clear performance expectations and success criteria

### 2. Domain-Specific Guidelines

```xml
<review_guidelines>
1. Analyze algorithmic complexity (Big-O notation)
2. Identify N+1 query problems
3. Check for caching opportunities
4. Assess memory usage patterns
5. Recommend performance optimizations
6. Estimate performance impact with data size
</review_guidelines>
```

**Why this matters:**
- Not generic "check for issues" - uses performance engineering terminology
- Specific to performance domain (Big-O, N+1, caching)
- Each guideline is measurable and actionable
- Covers the full spectrum of performance concerns

### 3. Performance-Specific Output Format

```xml
<issue>
  <current_complexity>O(n²)</current_complexity>
  <improved_complexity>O(n)</improved_complexity>
  <optimization>Use join query with single database call</optimization>
</issue>
```

**Why this matters:**
- Includes complexity analysis (quantifiable improvement)
- Shows before/after optimization (clear value proposition)
- Quantifies improvement (not just "faster")
- Enables data-driven decisions

### 4. Impact Estimation

```
6. Estimate performance impact with data size
```

**Why this matters:**
- Not just "it's slow" - provides actual numbers
- Example: "With 1000 posts, this takes 30s vs 0.3s optimized"
- Business impact is clear and measurable
- Helps prioritize optimization work

### 5. Customization Template Pattern

**The solution demonstrates** how to adapt the base template for different focus areas:
- Example shows performance focus
- Comments explain how to adapt for SRE or API design
- Demonstrates the pattern that applies to any domain

## 📊 Expected AI Output for Performance Review

### Complexity Analysis

```
Current Analysis:
- O(n) for loop iterations over user.post_ids
- Each Post.query.get(post_id) is a separate DB query = O(1) per query
- Each Like.query.filter_by(post_id).count() is another query = O(1) per query
- Total: O(n) loop × 2 queries per iteration = 2n database round trips

Performance Impact:
- With network latency: ~50ms per query
- For 1000 posts: 50ms × 2000 queries = 100 seconds!
- This is O(n) in queries, which is unacceptable for production
```

### N+1 Query Problem Identification

```
Line 4-5: Loop makes n queries for posts (N+1 problem #1)
  for post_id in user.post_ids:
      post = Post.query.get(post_id)  # Query executed n times

Line 6: Makes n additional queries for likes (N+1 problem #2)
  like_count = Like.query.filter_by(post_id=post.id).count()  # Query executed n times

Total queries: 1 (user) + 1000 (posts) + 1000 (likes) = 2001 queries
Classic N+1 problem (actually N+N+1 in this case)
```

### Optimization Recommendation

```python
def get_user_posts_with_likes_optimized(user_id):
    """Optimized version using SQL joins"""
    from sqlalchemy import func
    
    # Single query with join and aggregation
    posts_with_likes = db.session.query(
        Post,
        func.count(Like.id).label('like_count')
    ).join(
        Like, Like.post_id == Post.id, isouter=True
    ).filter(
        Post.user_id == user_id
    ).group_by(
        Post.id
    ).all()
    
    return posts_with_likes

# Performance improvement:
# Before: 2001 queries × 50ms = 100 seconds
# After: 1 query × 50ms = 0.05 seconds
# Improvement: 2000x faster!
```

### Additional Performance Considerations

**Caching Strategy:**
```python
# Add Redis caching for frequently accessed data
@cache.memoize(timeout=300)  # Cache for 5 minutes
def get_user_posts_with_likes_cached(user_id):
    return get_user_posts_with_likes_optimized(user_id)

# Result: Subsequent requests served from cache in ~1ms
```

**Database Indexing:**
```sql
-- Add indexes to speed up joins
CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_likes_post_id ON likes(post_id);

-- Further reduces query time from 50ms to ~5ms
```

**Pagination:**
```python
# Don't load all 1000 posts at once
def get_user_posts_paginated(user_id, page=1, per_page=20):
    return get_user_posts_with_likes_optimized(user_id)\
        .limit(per_page)\
        .offset((page-1) * per_page)

# Load 20 posts at a time instead of 1000
# Initial load: 5ms instead of 50ms
```

## 🔄 Adaptation Patterns for Other Focus Areas

### For SRE/Observability Review

```python
# Template customization for SRE focus
ReviewTemplate(
    role="Site Reliability Engineer specializing in observability",
    
    guidelines=[
        "Check for structured logging (not print statements)",
        "Verify metrics/tracing instrumentation",
        "Assess error handling and graceful degradation",
        "Review retry logic and circuit breakers",
        "Check for proper resource cleanup (connections, files)",
        "Verify timeouts and deadlines are set"
    ],
    
    output_format="""
    <observability_review>
      <logging_score>1-5</logging_score>
      <metrics_gaps>Missing metrics</metrics_gaps>
      <error_handling>Issues found</error_handling>
      <resilience_patterns>Circuit breakers, retries, etc.</resilience_patterns>
      <recommendations>Specific improvements</recommendations>
    </observability_review>
    """
)
```

**Example SRE Findings:**
```markdown
❌ Line 7: Using print() instead of structured logger
   Recommendation: Use logger.info() with structured fields

❌ Line 12: No timeout on database query
   Recommendation: Add timeout=5 to prevent hanging

❌ No circuit breaker on external API call
   Recommendation: Wrap with @circuit_breaker(failure_threshold=5)

✅ Good: Proper error handling with specific exceptions
```

### For API Design Review

```python
# Template customization for API design
ReviewTemplate(
    role="API Architect specializing in RESTful design",
    
    guidelines=[
        "Verify RESTful conventions (proper HTTP methods)",
        "Check status codes are semantically correct",
        "Assess API versioning strategy",
        "Review error response structure",
        "Check for backward compatibility",
        "Verify request/response schemas",
        "Assess pagination and filtering"
    ],
    
    output_format="""
    <api_review>
      <rest_compliance>Issues with REST conventions</rest_compliance>
      <breaking_changes>List of breaking changes</breaking_changes>
      <versioning_assessment>Version strategy evaluation</versioning_assessment>
      <error_handling>Error response quality</error_handling>
      <recommendations>API improvements</recommendations>
    </api_review>
    """
)
```

**Example API Design Findings:**
```markdown
❌ Line 3: POST /api/user/<id>/profile for updates
   Issue: Should use PUT or PATCH for updates, not POST
   Recommendation: Change to PATCH /api/user/<id>/profile

❌ Line 18: Returns 200 for errors
   Issue: Should return 4xx/5xx status codes for errors
   Recommendation: Return 400 for validation errors, 404 for not found

❌ No API versioning in URL or headers
   Issue: Can't evolve API without breaking clients
   Recommendation: Add /v1/ to URL path: /api/v1/user/<id>/profile

⚠️ Breaking change: Removed 'bio' field from response
   Impact: Existing clients will fail
   Recommendation: Deprecate gradually with version bump
```

### For Frontend/React Review

```python
# Template customization for React performance
ReviewTemplate(
    role="Senior Frontend Engineer specializing in React performance",
    
    guidelines=[
        "Check for unnecessary re-renders",
        "Verify proper use of useCallback/useMemo",
        "Identify missing key props in lists",
        "Assess component code splitting opportunities",
        "Check for useEffect dependency issues",
        "Review state management patterns",
        "Identify bundle size optimization opportunities"
    ],
    
    output_format="""
    <react_review>
      <rerender_issues>Unnecessary re-renders identified</rerender_issues>
      <hooks_misuse>useEffect, useMemo, useCallback issues</hooks_misuse>
      <performance_score>1-5</performance_score>
      <bundle_impact>Estimated bundle size impact</bundle_impact>
      <recommendations>Specific React optimizations</recommendations>
    </react_review>
    """
)
```

## 🎯 Key Takeaway: Same Structure, Different Focus

The power of template customization is that you keep the same **structure** but change the **domain-specific elements**:

| Template Element | Base | Performance | SRE | API Design |
|------------------|------|-------------|-----|------------|
| **Role** | Senior Engineer | Performance Engineer | Site Reliability Engineer | API Architect |
| **Guidelines** | General best practices | Big-O, N+1, caching | Logging, metrics, resilience | REST conventions, versioning |
| **Output** | Generic issues | Complexity analysis | Observability gaps | API compliance |
| **Severity** | blocker/major/minor | Performance impact (seconds/ms) | Incident risk (P0-P4) | Breaking changes vs non-breaking |
| **Evidence** | Code snippets | Profiling data, query counts | Missing telemetry | HTTP violations |
| **Success Criteria** | Code quality | Latency targets (< 100ms) | SLOs (99.9% uptime) | API standards compliance |

## 💡 When to Create Custom Templates

Create domain-specific templates when:

1. **Specialized Knowledge Required**
   - Security, performance, accessibility, compliance
   - Domain experts have specific checklists
   
2. **Different Standards Apply**
   - Mobile vs web performance targets
   - Public API vs internal API standards
   - Real-time systems vs batch processing

3. **Regulatory Requirements**
   - HIPAA compliance reviews
   - GDPR privacy checks
   - Financial services regulations

4. **Tool Integration Needed**
   - Output must feed into specific tools
   - Different metrics tracked per domain
   - Integration with domain-specific dashboards

## 🚀 Implementation Strategy

### Step 1: Start with Base Template
Use the general code review template as foundation

### Step 2: Identify Domain-Specific Elements
- What expertise does this domain require?
- What specific issues should be caught?
- What terminology is used?
- What metrics matter?

### Step 3: Customize Role and Guidelines
- Change role to domain expert
- Replace generic guidelines with domain-specific ones
- Add domain terminology and frameworks

### Step 4: Adapt Output Format
- Include domain-specific metadata
- Add measurements relevant to domain
- Structure for domain-specific tools

### Step 5: Test and Refine
- Test on known issues in the domain
- Measure detection accuracy
- Gather feedback from domain experts
- Iterate based on real usage

---

**Remember**: Customization doesn't mean starting from scratch. The core prompting techniques (role, structure, CoT, evidence requirements) remain the same. You're just changing the domain expertise and evaluation criteria.

