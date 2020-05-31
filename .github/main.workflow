action "ACTION1" {
  needs = "tests"
}

action "ACTION2" {
  needs = "deploy"
}