describe('Tests of frank-manual config - no warnings', () => {
  it('Test that there are no alerts in the status page', () => {
    cy.visitConsideringAuth('')
    // cy.get('[data-cy-status-alert]').should('have.length', 0)
    cy.tryToFindMoreThanZero('.alert-warning', 10)
  })

  it('Test that there are only alerts about FrankConfig-compatibility', () => {
    cy.visitConsideringAuth('')
    cy.tryToFindMoreThanZeroOmitting('.alert-warning', 'FrankConfig-compatibility', 10)
  })
})