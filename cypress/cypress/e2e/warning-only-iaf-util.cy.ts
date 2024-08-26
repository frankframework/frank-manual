describe('Tests of frank-manual config - only IAF_Util', () => {
  it('Test that the only alert in the status page is about config IAF-Util', () => {
    cy.visit('')
	  cy.get('.alert-warning').should('have.length', 1).within(() => {
      cy.contains('Configuration [IAF_Util]').should('have.length', 1)
    })
  })
})